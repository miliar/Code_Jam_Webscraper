
/*
14056
13999

14442743
13999999

1444444
1399999

145678
145669

13
132
1000
7
111111111111111110
14056
14442743
1444444
145678
199999
14467723
1
56789
234567899999999789
*/
#include <cstdio>
#include <vector>
#include <algorithm>

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        long long n;
        scanf("%I64d", &n);

        std::vector<int> a;
        for (; n > 0LL; n /= 10LL) a.push_back(n % 10LL);
        std::reverse(a.begin(), a.end());
        int i = 0;
        for (; i < a.size() - 1; i++)
            if (a[i] > a[i + 1]) break;
        if (i < a.size() - 1) {
            for (; i > 0 && a[i] == a[i - 1]; i--);
            a[i++]--;
            for (; i < a.size(); i++) a[i] = 9;
        }
        printf("Case #%d: ", cas);
        i = 0;
        for (; i < a.size() - 1 && a[i] == 0; i++);
        for (; i < a.size(); i++) printf("%d", a[i]);
        printf("\n");
    }
    return 0;
}
