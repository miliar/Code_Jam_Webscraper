#include <iostream>
#include <stdio.h>
using namespace std;
long long ultTidy(long long n);

int main(int argc, char *argv[]) {
	long long t, in;
	int caso=1;
	
	freopen("B-small.in","r",stdin);
	freopen("B-salidaSmall.out","w",stdout);
	cin>>t;
	while(t>0){
		cin>>in;
		if(in/10 == 0){
			cout<<"Case #"<<caso<<": "<<in<<endl;
			//printf("Case #%d: %ld\n",caso,in);
		}
		else{
			cout<<"Case #"<<caso<<": "<<ultTidy(in)<<endl;
			//printf("Case #%d: %ld\n",caso,);
		}
		
		
		caso++;
		t--;
	}
	
	
	
	return 0;
}

long long ultTidy(long long n){
	int ultDig=n%10;
	long long retorno=n;
	n/=10;
	
	while(true){
		
		while(n!=0){
			if( ultDig >=(n%10)){
				ultDig = n%10;
				n/=10;
			}else break;
		}
		
		if(n==0){
			return retorno;
			break;
		}else{
			retorno-=1;
			
			ultDig=retorno%10;
			n=retorno/10;
			
		}
	}
	
}




