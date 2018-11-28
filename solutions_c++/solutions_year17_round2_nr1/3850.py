#include<iostream>
#include<cmath>
#include<cstring>
#include<fstream>
#include<limits>
#include<iomanip>
using namespace std;


int main()
{
    fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\G_JAM01.txt");
    int T,case_count=1;
    cin>>T;
    
    while(T)
    {
       long long int D,N;
       cin>>D>>N;
       double init[N],speed[N];
       
       for(int i=0;i<N;i++)
       {
           cin>>init[i]>>speed[i];
       }
       
       double max_time=0,init_diff;
       
       for(int i=0;i<N;i++)
       {
           double time = (D-init[i])/speed[i];
           if(time>max_time)
           {
               max_time=time;
               init_diff = init[i];
           } 
       }
       
       long double fin_speed = D/max_time;
        
        int precision = std::numeric_limits<double>::max_digits10;
        std::cout <<fixed<<showpoint<<std::setprecision(precision) << fin_speed << std::endl;
        //cout<<"Case #"<<case_count<<": "<<fin_speed<<"\n";
        fil<<"Case #"<<case_count<<": "<<fixed<<showpoint<<std::setprecision(precision) << fin_speed << std::endl;
        case_count++;
        T--;
    }
    fil.close();
}
