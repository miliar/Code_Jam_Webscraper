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

int PPP;
int n;
vector<pair<int,int> > s;
vector<int> dms;

map<pair<vector<int>, int>, int> ans;
map<pair<vector<int>, int>, int>::iterator iter;

char st[MAX_CH];

int rec(int cur) {
    iter = ans.find(make_pair(dms,cur));
    if (iter != ans.end())
        return iter->second;

    int our_ans = 0;

    for (int i=0; i<PPP; i++)
        if (dms[i] > 0) {
            dms[i]--;
            int new_cur = (cur - i) % PPP;
            if (new_cur < 0) new_cur += PPP;

            int new_ans = rec(new_cur);

            dms[i]++;

            our_ans = max(our_ans, new_ans + (cur == 0));
        }

    ans[make_pair(dms,cur)] = our_ans;
    return our_ans;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	gets(st);
	sscanf(st,"%d",&tt);
	for (int qq=0; qq<tt; qq++) {
        cerr<<"\r"<<qq;
        scanf("%d%d",&n,&PPP);
        s.resize(n);
        dms.resize(PPP);
        for (int i=0; i<PPP; i++) dms[i] = 0;
        for (int i=0; i<n; i++) {
            scanf("%d",&s[i].first);
            s[i].second = s[i].first % PPP;
            dms[s[i].second]++;
        }

        ans.clear();
        int res = rec(0);

		printf("Case #%d: ",qq+1);
        printf("%d",res);
		printf("\n");
	}
	
	return 0;
}