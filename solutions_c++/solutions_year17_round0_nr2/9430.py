#include<iostream>
int main(void)
{
    int T,N,i,j,d,d1,d2,d3,d4;
    std::cout<<"Input \t\t\t\t\t Output\n";
    std::cin>>T;
    std::cout<<"\n";
    for(i=1;i<=T;i++)
    {
       std::cin>>N;
       for(j=N;j>0;j--)
      { d1=j%10;
       d=j/10;
       d2=d%10;
       d=d/10;
       d3=d%10;
       d=d/10;
       d4=d%10;
    if(d1>=d2&&d2>=d3&&d3>=d4)
   { std::cout<<"\t\t\t\t\t Case #"<<i<<":\t"<<j<<"\n";
      break;
      }
    } }

}