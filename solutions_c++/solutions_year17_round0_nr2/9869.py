//
//  qualification_B.cpp
//  CodeJamCPlusPlus
//
//  Created by Salal Mahmood on 09/04/2017.
//  Copyright © 2017 Salal Mahmood. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

bool isTidy(long long num)
{
    int last = 9;
    int n = 1;
    while(num)
    {
        int temp = num%10;
        if(temp > last)
            return false;
        
        last = temp;
        num = num/10;
    }
    
    return true;
}

long long pow(int n)
{
    long long out = 1;
    for(int i=0;i<n;i++)
        out*=10;
    
    return out;
}

long long nines(int num)
{
    long long out=0;
    for(int i=0;i<num;i++)
        out = out*10+9;
    
    return out;
}

long long makeTidy(long long num)
{
    int i=1;
    
    for(i=1;i<19;i++)
    {
        if( ((num/pow(i))%10) > ((num/pow(i-1))%10) )
        {
            num -= pow(i);
            num /= pow(i);
            num *= pow(i);
            num += nines(i);
            i=1;
        }
    }
    return num;
}

int main(int argc, const char * argv[]) {
    
    int count;
    
    
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    //in.open("input.txt");
    
    freopen("out.txt","w",stdout);
    
    
    in>>count;
    
    long long num = 0;
    
    for(int i=0; i<count; i++)
    {
        long long j;
        
        printf("Case #%d: ",i+1);
        in>>num;
        
        
        /*for(j=num; j>0; j--)
        {
            if(isTidy(j))
                break;
        }*/
        num = makeTidy(num);
        
        printf("%llu\n", num);
        
    }
    
    in.close();
    
    return 0;
}

