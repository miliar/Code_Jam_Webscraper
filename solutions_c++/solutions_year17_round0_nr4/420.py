#include <cstdio>
#include <vector>

using namespace std;

char s[2];
char c[101];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, m, ans, p = 0, j, k;
        vector <pair<char, pair<int, int> > > v;
        
        scanf("%d %d", &n, &m);
        
        for (j = 0; j < n; j++) c[j] = '.';
        
        for (j = 0; j < m; j++) {
            int y;
            
            scanf("%s %*d %d", s, &y);
            
            y--;
            
            c[y] = s[0];
            
            if (s[0] != '+') p = y;
        }
        
        for (j = 0; j < n; j++) {
            if (j == p) {
                if (c[j] != 'o') v.push_back(make_pair('o', make_pair(0, j)));
            } else if (c[j] == '.') {
                v.push_back(make_pair('+', make_pair(0, j)));
            }
        }
        
        if (p == 0) {
            for (j = 1; j < n; j++) v.push_back(make_pair('x', make_pair(j, j)));
        } else {
            for (j = n - 1, k = 0; j >= 1; j--) {
                if (k == p) k++;
                v.push_back(make_pair('x', make_pair(j, k++)));
            }
        }
        
        for (j = 1; j < n - 1; j++) v.push_back(make_pair('+', make_pair(n - 1, j)));
        
        if (n == 1) {
            ans = 2;
        } else {
            ans = n * 3 - 2;
        }
        
        printf("Case #%d: %d %d\n", i + 1, ans, v.size());
        for (j = 0; j < v.size(); j++) printf("%c %d %d\n", v[j].first, v[j].second.first + 1, v[j].second.second + 1);
    }
    
    return 0;
}
