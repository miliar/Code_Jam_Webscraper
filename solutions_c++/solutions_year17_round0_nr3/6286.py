#include <iostream>
#include <queue>

using namespace std;
 
int main(){
    freopen("small13.in", "r", stdin);
    freopen("outS13.txt", "w", stdout);
	int t, ls, rs, n, k;
	cin>>t;
	for(int i=0;i<t;i++){
		priority_queue<int> maxheap;
		cin>>n>>k;
		int pos = 1, l = n;
		while(pos<=k && l>0){
			if(!maxheap.empty()){
				l = maxheap.top();
				maxheap.pop();
			}
			if(l>0){
                ls = (l%2==0)?((l/2)-1):((l-1)/2);
                rs = (l%2==0)?(l/2):((l-1)/2);
			}
 
			maxheap.push(rs);
			maxheap.push(ls);
			pos++;
		}
		cout<<"Case #"<<i+1<<": "<<rs<<" "<<ls<<endl;
	}
	return 0;
}