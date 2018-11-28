/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: laura
 *
 * Created on April 8, 2017, 9:17 AM
 */
#include <cstdlib>
#include <iostream>

using namespace std;

/*
 * 
 */
bool isTidy(int* n,int l)
{
    bool check=true;
    for(int i=0;i<l-1;i++)
    {
        if(n[i]>n[i+1])
        {
            check=false;
            i=l;
        }
    }
    return check;
}

void testCase(long long int N)
{
    long long int copy=N;
    int n=0;
    while(copy)
    {
        n++;
        copy=copy/10;
    }
    copy=N;
    int* nt=new int[n];
    for(int i=n-1;i>=0;i--)
    {
        nt[i]=copy%10;
        copy=copy/10;
    }
    if(isTidy(nt,n))
        cout<<N;
    else
    {
        while(!isTidy(nt,n))
        {
        int ch=0;
        for(int i=0;i<n-1;i++)
        {
            if(nt[i]>nt[i+1] && ch==0)
            {
                nt[i]--;
                ch=9;
            }
            if(ch>0)
            {
                nt[i+1]=ch;
            }
        }
        }
        
        for(int i=0;i<n;i++)
           if(nt[i]>0) cout<<nt[i];
    }
    cout<<endl;
        
    
}

void input(int T)
{
   long long int N;
    for( int i=0; i<T; i++)
    {
        cin>>N;
        cout<<"Case #"<<i+1<<": ";
        if(N%10==N)
            cout<<N<<endl;
        else testCase(N);
    }
    
}

int main(int argc, char** argv) {

    int T;
    cin>>T;
    input(T);
    return 0;
}