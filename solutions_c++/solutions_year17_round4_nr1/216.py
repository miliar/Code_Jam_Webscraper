#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;


int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		int n, p;
		cin >> n >> p;
		if(p==2){
			int a=0;
			int b=0;
			for(int i=0; i<n; i++){
				int x;
				cin >> x;
				if(x%2==0) a++;
				if(x%2==1) b++;
			}
			int ans=0;
			while(a>=1){
				a--;
				ans++;
			}
			while(b>=2){
				b-=2;
				ans++;
			}	
			if(b==1){
				ans++;
			}
			cout << "Case #" << i << ": " << ans << endl;
		}
		if(p==3){
			int a = 0;
			int b = 0;
			int c = 0;
			for(int i=0; i<n; i++){
				int x;
				cin >> x;
				if(x%3==0) a++;
				if(x%3==1) b++;
				if(x%3==2) c++;
			}
			int ans=0;
			while(a>=1){
				a--;
				ans++;
			}
			while(b-c>=3){
				b-=3;
				ans++;
			}
			while(c-b>=3){
				c-=3;
				ans++;
			}
			while(c>=1 && b>=1){
				b--;
				c--;
				ans++;
			}
			if(b>=1||c>=1){
				ans++;
			}
			cout << "Case #" << i << ": " << ans << endl;
		}
		if(p==4){
			int a = 0;
			int b = 0;
			int c = 0;
			int d = 0;
			for(int i=0; i<n; i++){
				int x;
				cin >> x;
				if(x%4==0) a++;
				if(x%4==1) b++;
				if(x%4==2) c++;
				if(x%4==3) d++;
			}
			int ans=0;
			while(a>=1){
				a--;
				ans++;
			}
			while(c>=2){
				c-=2;
				ans++;
			}
			while(b>=1 && d>=1){
				b--;
				d--;
				ans++;
			}
			while(b>=4){
				b-=4;
				ans++;
			}
			while(d>=4){
				d-=4;
				ans++;
			}
			if(c==1 && b>=2){
				c--;
				b-=2;
				ans++;
			}
			if(c==1 && d>=2){
				c--;
				d-=2;
				ans++;
			}
			if(c>=1 || b>=1 || d>=1){
				ans++;
			}
			cout << "Case #" << i << ": " << ans << endl;
		}
		
	}	
}
