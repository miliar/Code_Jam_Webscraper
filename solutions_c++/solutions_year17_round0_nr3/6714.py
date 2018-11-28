#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main(){
	long long int n,t,k,j,i,x,y;
	
	//cin>>n>>k;
	ifstream myfile("c.txt");
ofstream outFile("output2.txt");
    myfile >> x;
    t=x;
    long long int a[t],b[t];
    i=0;
    while (myfile >> x >> y)
    {
       //cout<<x<<" "<<y<<endl;
       a[i]=x;
       b[i]=y;
       i++;
    }
    for(j=0;j<t;j++){
	n=a[j];
	k=b[j];
//	cout<<n<<" "<<k<<endl;
vector<long long int> v;
    v.push_back(n);
    for(int i=1;i<k;i++){
    	n=v[v.size()-1];
    	v.pop_back();
    	if(n%2==0){
    		v.push_back(n/2);
    		v.push_back(n/2-1);
    		sort(v.begin(),v.end());
		}
		else{
			v.push_back((n-1)/2);
    		v.push_back((n-1)/2);
    		sort(v.begin(),v.end());
		}
	}
	n=v[v.size()-1];
	if(n%2==0){
    		x=n/2;
    		y=n/2-1;
		}
		else{
			x=(n-1)/2;
			y=x;
		}
		outFile <<"Case #"<<j+1<<": "<< x <<" "<<y<<endl;
	//cout<<"            "<<x<<" "<<y<<endl;
	
}
	return 0;
}
