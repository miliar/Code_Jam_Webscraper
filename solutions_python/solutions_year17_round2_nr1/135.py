from __future__ import division


def reader(in_file):
    d, n = in_file.get_ints()
    horses = []
    for _ in xrange(n):
        horses.append(in_file.get_ints())
    return d, n, horses


def solver((d, n, horses)):
    MAX_time = 0
    for k, s in horses:
        totravel = d-k
        time = totravel / s
        MAX_time = max(MAX_time, time)

    return d/MAX_time

if __name__ == "__main__":
    # GCJ library publicly available at http://ideone.com/2PcmZT
    from GCJ import GCJ
    GCJ(reader, solver, "a", "A").run()
