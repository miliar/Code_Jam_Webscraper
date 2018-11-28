#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

long long calc(long long hm, long long h, long long a, long long c) {
    /*
    long long x, y;
    
    if (c == 1) return 1;
    if (a == 0) return c;
    if (hm <= a) return 1e18;
    if (hm <= a * 2) {
        if (c == 2) {
            if (h > a) {
                return 2;
            } else {
                return 1e18;
            }
        } else {
            return 1e18;
        }
    }
    
    x = h / a;
    if (h % a == 0) x--;
    
    if (x + 1 >= c) return c;
    
    y = hm / a - 1;
    if (hm % a == 0) y--;
    
    if ((c - x) % y == 0) {
        return c + (c - x) / y - 1;
    } else {
        return c + (c - x) / y;
    }
    */
    long long ans = 0;
    
    while (1) {
        ans++;
        
        if (c == 1) return ans;
        
        if (h <= a) {
            if (hm - a <= h) return 1e18;
            h = hm - a;
        } else {
            h -= a;
            c--;
        }
    }
}

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        long long hd, ad, hk, ak, b, d, x, y, c, h, a, sum = 0, ans = 1e18, j, k;
        vector <long long> v;
        
        scanf("%lld %lld %lld %lld %lld %lld", &hd, &ad, &hk, &ak, &b, &d);
        
        x = (hd + ak - 1) / ak;
        v.push_back(0);
        
        while (d > 0) {
            long long l = v.back(), r = 1e9, m = (l + r) / 2;
            
            while (r - l > 1) {
                if (d * m >= ak) {
                    r = m;
                    m = (l + r) / 2;
                } else {
                    long long y = (hd + ak - d * m - 1) / (ak - d * m);
                    
                    if (y > x) {
                        r = m;
                        m = (l + r) / 2;
                    } else {
                        l = m;
                        m = (l + r) / 2;
                    }
                }
            }
            
            v.push_back(r);
            
            if (d * r >= ak) break;
            
            x = (hd + ak - d * r - 1) / (ak - d * r);
        }
        
        x = (hk + ad - 1) / ad;
        y = 0;
        c = x;
        
        while (x > 1 && b > 0) {
            long long l = y, r = 1e9, m = (l + r) / 2;
            
            while (r - l > 1) {
                if (ad + b * m >= hk) {
                    r = m;
                    m = (l + r) / 2;
                } else {
                    long long y = (hk + ad + b * m - 1) / (ad + b * m);
                    
                    if (y < x) {
                        r = m;
                        m = (l + r) / 2;
                    } else {
                        l = m;
                        m = (l + r) / 2;
                    }
                }
            }
            
            if (ad + b * r >= hk) {
                x = 1;
            } else {
                x = (hk + ad + b * r - 1) / (ad + b * r);
            }
            y = r;
            c = min(c, x + r);
        }
        
        h = hd;
        a = ak;
        
        for (j = 0; j < v.size(); j++) {
            if (j == 0) {
                ans = min(ans, calc(hd, h, a, c));
            } else {
                long long x = v[j] - v[j - 1], y;
                
                for (k = 0; k < x; k++) {
                    if (h - a + d <= 0) {
                        if (hd - a <= h) break;
                        h = hd - a;
                        k--;
                        sum++;
                    } else {
                        a = max(a - d, 0LL);
                        h -= a;
                        sum++;
                    }
                }
                
                if (k < x) break;
                
                ans = min(ans, calc(hd, h, a, c) + sum);
            }
        }
        
        if (ans == 1e18) {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
        } else {
            printf("Case #%d: %lld\n", i + 1, ans);
        }
    }
    
    return 0;
}
