#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <set>
#include <utility>
#include <algorithm>
#include <ctime>
#include <map>
using namespace std;

int const MAX_N = 1024 * 1024;
int const MAX_CH = 5000010;
int const INT_INF = 1000000000;

int n,c,m;
vector<vector<int> > v;
int cnt[MAX_N];

char st[MAX_CH];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	gets(st);
	sscanf(st,"%d",&tt);
	for (int qq=0; qq<tt; qq++) {
        //cerr<<"\r"<<qq;
		
        scanf("%d%d%d",&n,&c,&m);
        v.clear();
        v.resize(c+5);
        int min_do = 0;
        for (int i=0; i<m; i++) {
            int pl, cc;
            scanf("%d%d",&pl,&cc);
            v[cc].push_back(pl);
        }
        for (int i=1; i<=c; i++)
            min_do = max(min_do, (int) v[i].size());

        for (int i=0; i<=n+5; i++) cnt[i] = 0;
        for (int i=1; i<=c; i++)
            for (int j=0; j<(int) v[i].size(); j++)
                cnt[v[i][j]]++;

        int is_Ok = 1;
        for (int i=1; i<=n; i++)
            if (cnt[i] > min_do) {
                is_Ok = 0;
                break;
            }

        if (is_Ok) {
            printf("Case #%d: ",qq+1);
            printf("%d %d",min_do,0);
		    printf("\n");
            continue;
        }

        long long down = min_do, up = 10000000;
        while (up > down) {
            long long mid = (up+down) / 2;

            int is_Ok = 1;
            int sum = 0;
            for (int i=1; i<=n; i++) {
                if (cnt[i] > mid) {
                    int rem = cnt[i] - mid;
                    if ((i-1)*mid - sum < rem) {
                        is_Ok = 0;
                        break;
                    }
                }
                sum += cnt[i];
            }

            if (is_Ok) up = mid;
            else down = mid + 1;
        }

        int do_cnt = 0;
        for (int i=1; i<=n; i++)
            if (cnt[i] > down)
                do_cnt += cnt[i] - down;

        printf("Case #%d: ",qq+1);
        printf("%lld %lld",(long long) down,(long long) do_cnt);
		printf("\n");
	}
	
	return 0;
}