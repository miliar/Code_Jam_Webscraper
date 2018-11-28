#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("/Users/abdulaleemkhan/Desktop/p2.txt");
    
    int cases;
    fin>>cases;
    unsigned long long  num = 0;
    for(int cc=0;cc<cases;cc++)
    {
        fin>>num;
        bool flag = true;
        bool f = true;
        while(f)
        {
            
            while(num>0)
            {
                int d1 = num%10;
                num/=10;
                int d2 = num%10;
                num/=10;
                if(d2>d1)
                {
                    flag = false;
                    break;
                }
            }
            if(flag)
            {
                cout<<"Case #"<<cc+1<<":"<<num<<endl;
                break;
            }
            else
                num--;
        }
    }
    
    return 0;
}
