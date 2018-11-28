#include <fstream>

using namespace std;

int main(void)
{
	ifstream in;
	ofstream out;
	in.open("in3.txt");
	out.open("out3.txt");
	int t;
	in >> t;
	for(int q=1;q<=t;q++){
		long long int a,b,c=1,p=0,kk,kk2,l,r;
		in >> a >> b;
		while(c<=b)
		{
			c*=2;
			p++;
		}
		kk2=a;
		kk=c;
		for(int e=0;e<p;e++) kk2/=2;
		l=kk2-1;
		r=kk2-1;
 		kk=(a/c)*c;
		long long int chai=a-kk,chai2=b-(c/2);
		if(chai>=chai2) l++;
		if(chai>=chai2+(c/2)) r++;
		out << "Case #"<<q<<": "<<l<<" "<<r<<endl;
		
	}
}
