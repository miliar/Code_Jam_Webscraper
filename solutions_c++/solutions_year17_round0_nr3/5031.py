#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	//fin.tie(NULL);
	//ifstream fin("ii.txt");
    //ofstream fout("output.txt");
	long long int t,n,k,count,left,num,right,var=0;
	cin>>t;
	while(t--){
		var++;
		cin>>n>>k;
		//int a[] = {n};
		priority_queue<int, vector<int> > v1;
		v1.push(n);
		//for(int i=0;i<=n;i++) a[i]=-1;
		//a[0]=n;
		//make_heap(v1.begin(), v1.end());
		for(int j=0;j<k;j++){
			int xyz = v1.top();
			//pop_heap(v1.begin(), v1.end());
			v1.pop();
			if(xyz%2==0){
				left=num=xyz/2;
				right=num-1;
				v1.push(num);
				if(num!=1)
				v1.push(num-1);
			}
			else{
				left=right=num = xyz/2;
				if(num!=0)
				{
					v1.push(num);
					v1.push(num);
				}
			}
			//push_heap(v1.begin(), v1.end());
		}
		cout<<"Case #"<<var<<": ";
		if(left==-1) left=0;
		if(right==-1) right=0;
		if(left>=right) cout<<left<<" "<<right;
		else cout<<right<<left;
		cout<<"\n";
	}
}
