#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;
ofstream myoutput("output.txt");
unsigned long long count=1;


class tidy{
private:
   unsigned long long num;
public:
    tidy(unsigned long long n):num(n){}
    vector<int> list;
    void sol(){
        while(num>0){
            list.push_back(num%10);
            num/=10;
        }
        bool istidy=false;
        int y=list.size();
        for(int i=y-1;i>0;i--){
            if(list[i]>list[i-1])
                istidy=false;
            else
                istidy=true;
        }
        for(int i=y-1;i>0;i--){
            if(list[i]>list[i-1]){
                if(list[i-1]==0 && list[i]==1){
                    list.pop_back();
                    int j=list.size();
                    while(j-1>=0){
                        list[j-1]=9;
                        j--;
                    }
                    break;
                }
                else  {
                    list[i]=list[i]-1;
                    int j=i-1;
                    while(j>=0){
                        list[j]=9;
                        j--;
                    }
                    break;
                }
            }
            else if(list[i]==list[i-1] && istidy==false){
                list[i]=list[i]-1;
                int j=i-1;
                while(j>=0){
                    list[j]=9;
                    j--;
                }
                break;
            }
        }
        int z=list.size();
        myoutput<<"Case #"<<count++<<": ";
        for(int i=z-1;i>=0;i--){
            myoutput<<list[i];
        }
        myoutput<<"\n";
    }
};

int main()
{
    ifstream file("input.txt");
    unsigned long long t;
    unsigned long long N;
    file>>t;
    while(t>0){
        file>>N;
        tidy x(N);
        x.sol();
        t--;
    }
}
