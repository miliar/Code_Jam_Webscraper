#include <bits/stdc++.h>
using namespace std;

int n,k;
int tc;

int main(){
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++ ){
		scanf("%d%d",&n,&k);
		priority_queue < pair < int , pair < int , int > > > q;
		
		q.push(make_pair(n,make_pair(-2,-(n+1))));
		while (1){
			k--;
			int z = q.top().first;
			int x = -q.top().second.first;
			int y = -q.top().second.second;
			q.pop();
			
			int mid =(x+y)/2;
			q.push(make_pair((mid-x),make_pair(-x,-(mid-1))));
			q.push(make_pair((y-mid),make_pair(-(mid+1),-y)));
			if ( k == 0 ){
				//cout << x << " " << y << endl;
				printf("Case #%d: %d %d\n",t,max(mid-x,y-mid),min(mid-x,y-mid));
				break;
			}
		}
	}
	fclose(stdout);
	return 0;
}
