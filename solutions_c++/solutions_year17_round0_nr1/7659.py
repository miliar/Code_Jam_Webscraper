#include <iostream>
#include<string.h>
using namespace std;

int main()
{
    int cases,K;
    string input;
    cin>>cases;
    for(int i=0 ;i< cases;i++){
    bool flag=true;
    cin>>input>>K;
    int answer=0;
    for(int j=0;j<= (input.length()-K);j++){
        if(input[j]=='-')
        {
            answer++;
            for(int k=j;k<j+K;k++)
                if(input[k]=='-')
                input[k]='+';
               else
                input[k]='-';
        }
    }
    for(int l = (input.length()-1),k=0 ;k < K && l >=0 ;l--,k++){
        if(input[l] =='-'){
            flag=false;
            break;
        }
    }


    if (flag){
    cout<<"Case #"<<i+1<<": "<<answer<<endl;
    }else{
    cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    }
    }
    return 0;
}
