#include<algorithm>
#include<iostream>
#include<fstream>
#define max 100000
using namespace std;
main()
{
	ifstream file_(".in");
	unsigned long long l,a[max],c=0,n,t,i,j,k,m,x,b[max],z=0;
	if(file_.is_open()){
	file_>>t;
	for(l=0;l<t;l++){
		file_>>x;
		for(n=x;n>=1;n--)
		{
		j=n;
		c=0;
		m=0;
		while(j>=1){
			a[m]=j%10;
			j=j/10;
		//	printf("%lld ",a[m]);
			m++;
		}
		
		for(i=m-1;i>=1;i--){
			if(a[i]>a[i-1]){
				c++;
			}
		}
		if(c==0){
			//printf("Case #%lld: %lld\n",l+1,n);
			/*ofstream file_;
			file_.open("cc.txt");
			if(file_.is_open()){
				file_<<"Case #"<<l+1<<": "<<n<<endl;
			    file_<<" PRint kyu nai ho raha"<<t;
			}*/
			b[z]=n;
			z++;
			break;
		}
	    }
	}
    ofstream file_;
			file_.open("cc.txt");
			if(file_.is_open()){
				for(i=0;i<z;i++){
				file_<<"Case #"<<i+1<<": "<<b[i]<<endl;
			}
			}
	
	file_.close();
	std::cin.get();	
	}
	
}