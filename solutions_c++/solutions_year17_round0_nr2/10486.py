#include<iostream>
bool isTidy(int n)
{
    int LastDigit = n%10;
    n= n/10;    
    while(n > 0)
    {
        int digit = n%10;
        if( digit > LastDigit )
            return false;
        LastDigit = digit;
        n= n/10;
        
    }
    return true;
}
int getLastTidyNo(int N)
{
    for( int i =N ;i >=0 ; i--)
    {
        if(isTidy(i))
            return i;
    }
    return 0;
}
int main()
{
    int T;
    std::cin>>T;
    int cse = 1 ;
    while(T--)
    {
        int N;
        std::cin>>N;
        std::cout<<"Case #"<<cse<<": "<<getLastTidyNo(N)<<"\n";
        cse++;
    }
    return 0;
}
