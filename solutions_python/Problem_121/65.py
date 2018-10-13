def max_gain(energy, regen, max_energy, activities, pos=0, cache = None):
    if pos == len(activities):
        return 0
    if cache is None:
        cache = {}
    key = (energy, pos)
    if key in cache:
        return cache[key]
    m_gain = 0
    for i in range(energy+1):
        remaining = min(max_energy, energy-i+regen)
        gain = i*activities[pos]
        gain += max_gain(remaining, regen, max_energy, activities, pos+1, cache)
        m_gain = max(gain, m_gain)
    cache[key] = m_gain
    return m_gain

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        E,R,N = map(int, raw_input().split())
        activities = map(int, raw_input().split())
        print "Case #%d: %d" % (i, max_gain(E, R, E, activities))
        
