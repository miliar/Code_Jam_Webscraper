#include <iostream>
#include <string> 
#include <set>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

bool isTidy(unsigned long long int val){
    string inp = to_string(val);
    //cout<<inp<<endl;
    bool res = true;
    stringstream sst;
    sst << inp[0];
    int val1,val2;
    sst >> val1;
    for(int i=1;i<inp.length();i++){
        stringstream ss;
        ss << inp[i];
        ss >> val2;
        //cout<<endl<<val1<<"-"<<val2<<endl;
        if(val2 >= val1){
            val1=val2;
        }else{
            res =false;
            break;
        }
    }
    return res;
}


int smallTidy(string smallTidy){
    stringstream ss;
    ss << smallTidy;
    int num;
    ss >> num;
    bool res = isTidy(num);
    while(!res)
            res = isTidy(--num);
    return num;
}

int main(){

    int T;
    cin >> T;
    for (int x=0;x<T;x++){
         string val,temp,result;
         cin >> val;
         temp = "";
         int size = val.length();
         result = val[val.size()-1];
         temp =result;
         for(int i=size-2;i>=0;i--){
            temp = val[i]+temp;
            result = val[i]+result;

            if(val[i]=='0')
                continue;
            //cout << temp;
            size_t found = temp.find('0');
            if(found != string::npos){
                for(int j=1;j<temp.size();j++)
                    result[j] = '9';
                if(i!=0)
                    result[0]= result[0]-1;
                else if(temp[0]=='1')
                    result.erase(0,1);
                else
                    result[0]= result[0]-1;
                temp = result[0];
                continue;
            }else{
                if(temp.length() == 2){               
                    temp = to_string(smallTidy(temp));
                    //cout<<"length is 2 - "<<temp<<endl;
                    result[0]=temp[0];
                    result[1]=temp[1];
                    temp = temp[0];
                }
            }
         }
         for(int i=1;i<result.length();i++){
             if(result[i] < result[i-1])
                result[i] = result[i-1];
         }
        cout << "Case #"<<x+1<<": "<<result<<endl;

    }

}