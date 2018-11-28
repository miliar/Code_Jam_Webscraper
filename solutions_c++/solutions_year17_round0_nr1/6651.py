#include <iostream>
using namespace std;

int main() {
  int test;
  cin>>test;
  for(int q=0;q<test;q++){
    char a[10000];
    int k,count=0;
    cin>>a;
    cin>>k;
    int len=0,flag=0;
    for(int i=0;a[i]!='\0';i++){
        len++;
    }
    for(int i=0;i<len;i++){
        if(a[i]=='-'){
            if(k<=(len-i)){
                count++;
            for(int p=i,j=0;j<k;p++,j++){
                    if(a[p]=='+'){
                       a[p]='-';
                    }else{
                        a[p]='+';
                    }
            }
        }
    }
    }
    for(int i=0;i<len;i++){
        if(a[i]=='-'){
            cout<<"Case #"<<q+1<<": IMPOSSIBLE"<<endl;
            flag=2;
            break;
        }
    }
    if(flag!=2){
        cout<<"Case #"<<q+1<<": "<<count<<endl;
    }
  }
	return 0;
}
