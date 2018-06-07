import matplotlib.pyplot as plt


def computeWindowBpm(data):
    aC = []
    dC = []
    dCSum = []
    dCMinLength = 0
    levels = 4
    maxDecimation = pow(2, levels-1)
    minIndex = (60. / 220 *  sampleRate.toDouble/maxDecimation).toInt
    maxIndex = (60. / 40 * sampleRate.toDouble/maxDecimation).toInt

    for loop in range(0, levels):
        transform = new Transform(new FastWaveletTransform(wavelet));
        if (loop == 0):
            coefficients = transform.decompose(data)
            l = coefficients.length - 1
            aC = coefficients(1).slice(0, coefficients(1).length/2)
            dC = coefficients(l).slice(coefficients(l).length/2, coefficients(l).length)
            dCMinLength = (dC.length/maxDecimation).toInt + 1
        else:
            coefficients = transform.decompose(aC)
            l = coefficients.length - 1
            aC = coefficients(1).slice(0, coefficients(1).length/2)
            dC = coefficients(l).slice(coefficients(l).length/2, coefficients(l).length)


        pace = pow(2, (levels-loop-1)).toInt
        dC = dC.undersample(pace).abs
        dC = dC - dC.mean


        if(dCSum == null):
            dCSum = dC.slice(0, dCMinLength)
        else:
            dCSum = dC.slice(0, min(dCMinLength, dC.length)) |+| dCSum

    aC = aC.abs
    aC = aC - aC.mean
    dCSum = aC.slice(0, min(dCMinLength, dC.length)) |+| dCSum

    correlated = dCSum.correlate
    correlatedTmp = correlated.slice(minIndex, maxIndex)

    location = detectPeak(correlatedTmp)

    realLocation = minIndex + location
    windowBpm= 60.toDouble / realLocation * (sampleRate.toDouble/maxDecimation)
    print("dwt tempo: " + windowBpm)
    instantBpm += windowBpm