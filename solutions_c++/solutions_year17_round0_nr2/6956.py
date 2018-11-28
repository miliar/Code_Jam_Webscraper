#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;
#define INF (1<<29)

int main(){
	int tc;
	string s;
	cin >> tc;
	for(int i=0;i<tc;i++){
		cin >> s;
		for(int j=s.length()-1;j>0;j--){
			for(int k=j-1;k>=0;k--){
				if(s[j]<s[k]){
					s[j]='9';
					for(int x=j-1;x>=0;x--){
						if(s[x]=='0'){
							s[x]='9';
						}
						else{
							s[x]=s[x]-1;
							break;
						}
					}
					for(int x=j;x<s.length();x++)s[x]='9';
					break;
				}
			}
		}
		if(s[0]=='0')s.erase(s.begin());
		cout << "Case #" << i+1 << ": " << s << endl;
	}
	return 0;
}
