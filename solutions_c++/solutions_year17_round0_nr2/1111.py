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

int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
	    printf("Case #%d: ",z+1);
		string s;
		cin>>s;
		int n = s.ln;
		while(true) {
            int untidy = -1;
            fore(i,0,n-1)
            {
                if(s[i]>s[i+1]) {
                    untidy = i;
                    break;
                }
            }
            if(untidy == -1) {
                break;
            }
            s[untidy] = (char)(s[untidy]-1);
            fore(i,untidy+1,n)
            {
                s[i] = '9';
            }
		}
		if(s[0] == '0') {
            s.erase(s.begin());
		}
		cout<<s<<endl;
	}
	return 0;
}
