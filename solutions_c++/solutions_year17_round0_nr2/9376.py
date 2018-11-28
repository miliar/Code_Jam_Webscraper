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

int main(){
	//ios_base::sync_with_stdio(false);cin.tie(NULL); cout.tie(NULL);
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	ll t, index, i, j;
	
	cin >> t;
	
	for(index=1; index<=t; index++){
		string str, ans="";
		cin >> str;
		str += '9'+1;
		ll size=siz(str);

		for(i=0; i<size-1; i++){
			//trace4(i, str[i], ans, size);
			if(str[i]==str[i+1]){
				//j=i+1;
				
				for(j=i+1; j<size-1; j++){
					if(str[j] < str[j+1]){
						break;
					} else if(str[j] > str[j+1]){
						break;
					}
				}
				//trace3(j, str[j], str[j+1]);
				if(str[j] > str[j+1]){
					ans += str[i]-1;
					for(i=i+1; i<size-1; i++){
						ans += '9';
					}
				} else{
					for(; i<size-1; i++){
						ans += str[i];
					}
				}
			} else if(str[i] < str[i+1]){
				ans += str[i];
			} else{
				ans += str[i]-1;
				
				for(i++; i<size-1;i++){
					ans += '9';
				}
			}
		}
		//trace2(ans, size);
		cout << "Case #" << index << ": ";
		i=0;
		while(i<size-1 && ans[i]=='0'){
			i++;
		}
		
		while(i<size-1){
			cout << ans[i];
			i++;
		}
		cout << endl;
	}
	return 0;
}
