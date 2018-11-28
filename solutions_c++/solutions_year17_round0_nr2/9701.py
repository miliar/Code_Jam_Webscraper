#include <iostream>
using namespace std;

int main() {
        int a[100];
        int s,l,flag=0,slag=0,n,i,j,r,no,tc;
        cin>>tc;
        for(i=0;i<tc;i++){
            cin>>a[i];
        }
        for(i=0;i<tc;i++){
            for(j=a[i];j>0;j--){
                n = j;
                s = 0;
                l = n%10;
                flag=0;
                slag=0;
                while(n>0){
                    slag++;
                    r=n%10;
                    if(r<=l){
                        l=r;
                        flag++;
                    }
                    else{
                        break;
                    }
                    n=n/10;  
                }
                if(flag==slag){
                    no=i+1;
                    cout<<"Case #"<<no<<": "<<j<<endl;
                    break;
                }
            }
        }
	return 0;
}
