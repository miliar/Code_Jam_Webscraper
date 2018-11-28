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
	long long n,k;
	cin>>n>>k;
	priority_queue<int>q;
	q.push(n);
	int x;
	while (k--){
		x = q.top();
		q.pop();
		q.push((x-1)/2);
		q.push(x/2);
	} 
	cout<<(x/2)<<' '<<(x-1)/2<<endl;

}
int main(){
    freopen("C-small-2-attempt0.in.txt","r",stdin);freopen("a.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++cas){
        printf("Case #%d: ",cas);
        main_part();
    }
    return 0;
}
