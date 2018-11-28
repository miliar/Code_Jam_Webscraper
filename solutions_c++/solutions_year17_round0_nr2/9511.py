#include<iostream>
#include<deque>
using namespace std;

bool tidy(unsigned long long n)
{
	for(int d,p=9; n>0; n/=10) {
		d=n%10;
		if(p<d) return false;
		p=d;
	}
	return true;
}

unsigned long long pow10(int j)
{
	unsigned long long n=1;
	for(int i=j; i>0; i--) n*=10;
	
	return n;
}

void reduce(unsigned long long& num)
{
	unsigned long long i=0,n=num;
	deque<int> dnum;
	
	for(int d;n>0;n/=10) {
		d=n%10;
		dnum.push_front(d);
	}
	
	for(i=0; i<dnum.size()-1; i++) if(dnum[i]>dnum[i+1]) break;  
	dnum[i]--;                                                        
	for(unsigned j=i+1; j<dnum.size(); j++) dnum[j]=9;                
	for(int j=0;dnum.size();j++,dnum.pop_back()) n+=dnum.back()*pow10(j); 
	num=n;                                                         
}

int main()
{
	unsigned t;
	cin>>t;	
	
	unsigned long long n,last;
	for(unsigned i=1; i<=t; i++) {		
		cin>>n;
		
		for(unsigned long long j=n; j>=1; ){
			if(tidy(j)) {
				last=j;
				break;
			}
			reduce(j);			
		}
		cout<<"Case #"<<i<<": "<<last<<endl;
	}
	
	return 0;
}
