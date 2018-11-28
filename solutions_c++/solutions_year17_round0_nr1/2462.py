#include <iostream>
#include <string>
using namespace std;
int main()
{
    int ttt;
    cin>>ttt;
    for(int tttt = 1;tttt<=ttt;tttt++)
    {
        cout<<"Case #"<<tttt<<": ";
        char num[300] = {0};
        for(int i=0;i<300;i++)
            num[i]=0;
        cin>>num;
        int len = strlen(num);
        for(int i=0;i<len-1;i++)
        {
            if(num[i] > num[i+1])
            {
                for(int j=i+1;j<len;j++)
                {
                    num[j] = '9';
                }
                if(num[i] == '1')
                {
                    num[0] = '0';
                    for(int j =1;j<=i;j++)
                        num[j] = '9';
                    
                }
                else
                {
                    while(i>=1)
                    {
                        if(num[i] == num[i-1])
                        {
                            num[i] = '9';
                            i--;
                        }
                        else
                            break;
                        
                    }
                    num[i]--;
                }
               
                break;
            }
        }
        
        if(num[0] != '0')
            cout<<num[0];
        for(int i=1;i<len;i++)
        {
            cout<<num[i];
        }
        cout<<endl;
    }
}
