#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007

void answer(ll k)
{
    cout<<k/2<<" "<<(k-1)/2<<endl;
}
int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		ll n,k;
		cin>>n>>k;
		ll left = n, cur = 1, done = 0;
		while(true) {
            if(done+cur>=k) {
                ll atleast = left/cur;
                if(left%cur>=(k-done)) {
                    atleast++;
                }
                answer(atleast);
                break;
            }
            left-=cur;
            done+=cur;
            cur*=2;
		}
	}
	return 0;
}
