#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

const std::string bad = "IMPOSSIBLE";

bool check(int r, int y, int b)
{
    if (r < 0 || y < 0 || b < 0) return false;
    if (r < y) std::swap(r, y);
    if (r < b) std::swap(r, b);
    if (r > y + b) return false;
    return true;
}

std::string construct(std::vector<std::string> r,
        std::vector<std::string> y,
        std::vector<std::string> b)
{
    if (r.size() < y.size()) std::swap(r, y);
    if (r.size() < b.size()) std::swap(r, b);
    if (y.size() < b.size()) std::swap(y, b);

    for (int i = (int)y.size() - 1, j = (int)b.size() - 1; i >= 0 && j >= 0; -- i, -- j) {
        y.insert(y.begin() + i, b[j]);
        b.pop_back();
    }
    std::string ret;
    for (int i = 0, j = 0; i < r.size() || j < y.size(); ) {
        if (i < r.size()) ret += r[i ++];
        if (j < y.size()) ret += y[j ++];
    }
    return ret;

}

void append(std::vector<std::string> &v, int num, const std::string &s)
{
    for (int i = 0; i < num; ++ i)
        v.push_back(s);
}

void concact(std::string &s, int num, const std::string &t)
{
    for (int i = 0; i < num; ++ i)
        s += t;
}

std::string get(int w, std::string a, std::string b)
{
    std::string ret;
    concact(ret, w, a + b);
    return ret;
}

std::string solve()
{
    int n, r, o, y, g, b, v;
    std::cin >> n >> r >> o >> y >> g >> b >> v;
    if (r + g == n && r == g)
        return get(r, "R", "G");
    if (y + v == n && y == v)
        return get(y, "Y", "V");
    if (b + o == n && b == o)
        return get(b, "B", "O");
    if (!check(r - g, y - v, b - o)) return bad;
    for (int ri = 0; ri <= g && g + ri <= r; ++ ri) {
        if (!ri && g - ri) continue;
        for (int yi = 0; yi <= v && v + yi <= y; ++ yi) {
            if (!yi && v - yi) continue;
            for (int bi = 0; bi <= o && o + bi <= b; ++ bi) {
                if (!bi && o -  bi) continue;

                std::vector<std::string> rs, ys, bs;
                append(rs, ri, "RGR");
                concact(rs.back(), g - ri, "GR");
                append(rs, r - g - ri, "R");
                append(ys, yi, "YVY");
                concact(ys.back(), v - yi, "VY");
                append(ys, y - v - yi, "Y");
                append(bs, bi, "BOB");
                concact(bs.back(), o - bi, "OB");
                append(bs, b - o - bi, "B");

                return construct(rs, ys, bs);
            }
        }
    }
    return bad;
}

int main()
{
    int cas;
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ ca) {
        printf("Case #%d: %s\n", ca, solve().c_str());
    }
}
