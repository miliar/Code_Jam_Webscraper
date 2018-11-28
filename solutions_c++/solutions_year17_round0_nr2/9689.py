#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	fstream myfile;
 	ofstream outfile("output.txt");
  	//set<int> vtr;
  	myfile.open ("input.txt");
  	int tests;
  	myfile>>tests;
  	for(int i=1;i<=tests;i++){
        int n;
        myfile>>n;
        int flag =0;
        for(;n>0&&flag==0;n--){
            flag=1;
            int m =n;
            int a = m%10;
            m = m/10;
            while(m!=0&&flag==1){
                int b=m%10;
                m=m/10;
                if(a<b)
                    flag=0;
                a=b;
            }
            
        }
        outfile<<"Case #"<<i<<": "<<n<<endl;
        
        continue;
        
    }
	return 0;
}