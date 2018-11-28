#include <iostream>
#include <queue>
using namespace std;
int main(){
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
	int nn;
	cin>>nn;
	int ii=0;
	while(ii<nn){
		cout<<"Case #"<<ii+1<<": ";
		long long n;
		int k;
		cin>>n>>k;
		priority_queue<long long> q;
		while(!q.empty())q.pop();
		q.push(n);
		for(int i=0;i<k;i++){
			long long tmp=q.top();
			q.pop();
			if(tmp&1){
				q.push(tmp>>1);
				q.push(tmp>>1);
				if(i==k-1){
					cout<<(tmp>>1)<<' '<<(tmp>>1);
				}
			}
			else{
				q.push(tmp>>1);
				q.push((tmp-1)>>1);
				if(i==k-1){
					cout<<(tmp>>1)<<' '<<((tmp-1)>>1);
				}
			}
		}
		
		cout<<endl;
		ii++;
	}

}
