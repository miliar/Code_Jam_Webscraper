//Yahoo

#include<iostream>
#include<set>
using namespace std;

multiset<int> len;

int main(){
	int T;
	cin>>T;
	for(int Test=1;Test<=T;Test++){
		int n,k;
		cin>>n>>k;
		len.clear();
		len.insert(n);
		int a,b;
		for(int i=0;i<k;i++){
			int biggest=*(--len.end());
			len.erase(--len.end());
			a=b=(biggest-1)/2;
			if(biggest%2==0)
				b++;
			if(a)
				len.insert(a);
			if(b) 
				len.insert(b);
		}
		cout<<"Case #"<<Test<<": "<<b<<" "<<a<<endl;
	}
}
