#include <iostream>
#include<sstream>


using namespace std;

bool check(string num){
    for(int i=0;i<num.length()-1;i++){
        if(num[i]>num[i+1]){
            return false;
        }
    }
    return true;
}

int main()
{   int n,no;
    cin>>n;
    string number;
    bool res=false;
    for(int i=1;i<=n;i++){
        res=false;
        cin>>no;

        while(no>=1 && res==false){
            //number=string(no);
            stringstream ss;
            ss<<no;
            number=ss.str();
            res=check(number);
            --no;
        }
        cout<<"Case #"<<i<<": "<<++no<<endl;

    }


    return 0;
}


