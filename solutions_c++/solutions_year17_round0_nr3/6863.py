#include <bits/stdc++.h>
using namespace std;
int cazul=1;
bool visited[10101];
int r[1001],l[1001];		
ofstream fout("output.out");

int func(int n, int k){
		//cout << n << ' ' << k << endl;
		memset(r,0,sizeof(r));
		memset(l,0,sizeof(l));
		memset(visited,0,sizeof(visited));
		for(int i=2;i<=n;i++)
			l[i]=l[i-1] + 1;
		for(int i=n-1;i>=1;i--)
			r[i]=r[i+1]+1;
		for(int i=1;i<=k;i++){
			int pos = -1;
			int mini = -1;
			int maxi = -1;
			int a,b;
			for(int j=1;j<=n;j++){
					if(visited[j])
						continue;
					int currMin = min(r[j], l[j]);
					if(mini < currMin){
						mini = currMin;
						maxi = max(r[j], l[j]);
						pos = j;
						a=l[j];b=r[j];
					} else 
					if(mini == currMin){
						int currMax = max(l[j],r[j]);
						if(currMax > maxi){
							pos = j;
							maxi = currMax;
							a=l[j];b=r[j];
						} else 
						if(currMax == maxi){
							if(j < pos){
								pos = j;
								a=l[j];b=r[j];

							}
						}
					} 
			}
			visited[pos] = true;
			int acc = 0;
			for(int j=1;j<=n;j++){
				if(visited[j]){
					acc = 0;
					continue;
				}
				l[j] = acc;
				acc++;
			}
			acc = 0;
			for(int j=n;j>=1;j--){
				if(visited[j]){
					acc = 0;
					continue;
				}
				r[j] = acc;
				acc++;
			}
			if(i == k){
				fout << "Case #" << cazul << ": "<<  max(a,b) << ' ' << min(a,b) << endl;
				cazul++;
			}
		}

		return(0);
}


int main(){
	ifstream cin("C-small-1-attempt0.in");
	int t;
	cin >> t;
	for(int j=0;j<t;j++){
						int n,k;
						cin >> n >> k;
						func(n, k);
	}
	return(0);
}
