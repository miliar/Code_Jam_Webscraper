#include<iostream>
#include<cstring>
#include<stdio.h>

void sol(std::string S,int z)
{
    for(int i=0;i<S.length()-1;++i)
    {
      if(S[i]>S[i+1])
      {
        S[i]=S[i]-1;
        for(int j=i+1;j<S.length();++j)
          S[j]='9';
        i=i-2;
      }

    }
    printf("Case #%d: ",z);
    if(S[0]!='0') printf("%c",S[0]);
    for(int i=1;i<S.length();++i)
      printf("%c",S[i]);
    //std::cout<<S<<"\n";
}
int main()
{
  int T;
  scanf("%d",&T);
  int i=1;
  while(T--)
  {
    std::string S;
    std::cin>>S;
    sol(S,i);
    ++i;
    printf("\n");
  }
  return 0;
}