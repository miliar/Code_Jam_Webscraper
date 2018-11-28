#include <iostream>
#include <math.h>
using namespace std;
int main() {
 long long int t, n,a,j,k;
  cin >> t;
  for(j=0;j<t;j++)
  {
  	cin>>n;
  	a=n;
  	int i=1;
  	while(a){
         double kkkk=(pow(10,i+1));
         double kkk=(pow(10,i));
        double kk=(pow(10,i-1));
        long long int hhhh=kkkk;
        long long int hh=kk;

        long long int hhh=kkk;


        long long int aaaaa;
        long long int aa=n%(hhh);
        if(i!=1)
            aaaaa=aa/hh;
        else
            aaaaa=aa;
        long long int aaa=n%hhhh;

        long long int aaaa=aaa/hhh;
        if(aaaa>aaaaa){
                double bb=pow(10,i);
            n=n-(n%hhh+1);
        }

    i+=1;
    a=a/10;
  	}
  	cout<<"case #"<<(j+1)<<":"<<n<<endl;
   }
  return 0;
}

