#include<bits/stdc++.h>

#define X first
#define Y second
#define eb push_back
#define pb pop_back
#define siz(a) int(a.size())
//for traversing the container (bcoz we cannot access linked list etc with direct index)
//c stands for container and it for iterator
#define tr(c, it) \
		for(typeof(c.begin()) it=c.begin() ; it != c.end() ; it++)
		
#define all(c) c.begin(), c.end()
#define present(container, element) (container.find(element) != container.end()) //whether the element is present in the container

#define trace2(x, y)             cout <<#x<<": "<<x<<" | "<<#y<<": "<<y<< endl;
#define trace3(x, y, z)          cout <<#x<<": "<<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl;
#define trace4(a, b, c, d)       cout <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;
#define trace5(a, b, c, d, e)    cout <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<<": "<<e<<endl;
#define scan(x) scanf("%lld", &x)
#define print(x) printf("%lld", x)
#define pN printf("\n");
using namespace std;

typedef long long int ll;
typedef vector < int > vi;
typedef vector < vi > vvi;
typedef vector < ll > vll;
typedef vector < vll > vvll;

typedef pair < int , int > ii;

const int mod=1e9+7;
const int maxn=1e4+5;

ll q[maxn];

int main(){
//	ios_base::sync_with_stdio(false);cin.tie(NULL); cout.tie(NULL);
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	ll t, k, i, n, j;
	cin >> t;
	
	for(n=1; n<=t; n++){
		
		string str;
		
		cin >> str >> k;
		
		ll size = siz(str), ans=0;
		
		for(i=0; i<size; i++){
			if(str[i]=='-')
				q[i]=0;
			else
				q[i]=1;
		}
		
		for(i=0; i<size; i++){
			//trace3(i, q[i], ans);
			if(!q[i]){
				if(i+k <= size){
					for(j=i; j<i+k; j++){
						//trace2(j, q[j]);
						q[j] ^= 1;
					}
					ans++;
				}
			}
		}
		
		bool flag=true;
		
		for(i=0; i<size; i++){
			//trace2(i, q[i]);
			if(!q[i]){
				flag=false;
				break;
			}
		}
		cout << "Case #" << n << ": " ;
		if(flag)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
