#include<iostream>
#include<cmath>
#include<cstring>
#include<fstream>
using namespace std;

bool resolved(int a[],int count)
{
    for(int i=0;i<count-1;i++)
    {
        if(a[i]<a[i+1])
        return false;
    }
    return true;
}
int main()
{
    fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\G_JAM02.txt");
    int T,case_count=1;
    cin>>T;
    
    while(T)
    {
        long long int N;
        cin>>N;
        int num[19],digit=0;
        
        while(N>0)
        {
            int tmp = N % 10;
            num[digit]=tmp;
            digit++;
            N/=10;
        }
        
        int k=digit; 
        while(!resolved(num,digit)) 
        {
            if(k-1>0 && num[k-1] > num [k-2] )
            {
                
                num[k-1]--;
                for(int j=0;j<k-1;j++)
                num[j]=9;
                
                int t=k-1;
                while(t<digit-1 && num[t] < num[t+1])
                {
                    num[t]=9;
                    num[t+1]--;
                    t++;
                }
                
            }
                  
            k--;
        }
        
        long long int fin=0;
        for(int i=digit-1;i>=0;i--)
        fin = fin*10 + num[i];
        
        cout<<"Case #"<<case_count<<": "<<fin<<"\n";
        fil<<"Case #"<<case_count<<": "<<fin<<"\n";
        case_count++;
        T--;
    }
    fil.close();
}
