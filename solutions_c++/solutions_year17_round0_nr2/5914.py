#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <iostream>

using namespace std;


const int maxn = 1e5 + 10;
const int MOD = 1e9 + 7;
const double eps = 1e-7;
const int INF = 2e9;



void main_part(){
	long long n;
	cin>>n;
	long long nn = n;
	long long ans = 0;
	int a[20];
	a[0] = -1;
	for (int i = 1; i <= 18; ++i){
		a[i] = n % 10;
		n /= 10; 
	}
	int start = 18;
	while (a[start] == 0){
		start--;
	}
	int tmp = start;
	while (a[tmp-1] >= a[tmp]){
		tmp--;
	}
	if (tmp == 1){
		cout<<nn<<endl;
		return;
	}
	for (int i = tmp - 1; i >= 1; --i){
		a[i] = 9;
	}
	a[tmp]--;
	while (a[tmp] < a[tmp+1]){
		a[tmp] = 9;
		a[tmp+1]--;
		tmp++;
	}
	for (int i = 18; i >= 1; --i){
		ans = ans * 10 + a[i];
	}
	cout<<ans<<endl;
}
int main(){
    freopen("B-small-attempt0.in.txt","r",stdin);freopen("a.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++cas){
        printf("Case #%d: ",cas);
        main_part();
    }
    return 0;
}

