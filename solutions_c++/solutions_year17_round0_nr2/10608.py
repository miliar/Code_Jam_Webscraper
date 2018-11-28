#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int digitsNum(int x);
int is_tidy(int digits,int num);
int main()
{
    ifstream cin("B-small-attempt1.in");
    ofstream cout("New Text Document.out");
     int size;
     cin >> size;
     int *arr = new int[size];
     int *arr_tidy=new int[size];
     for(int i=0;i<size;i++)
        {
            cin>>arr[i];
        }


        for(int i=0;i<size;i++)
        {
                while(arr[i]>0)
                {
                    int digitNum=digitsNum(arr[i]);
                    if(is_tidy(digitNum ,arr[i]))
                        {
                            arr_tidy[i]=arr[i];
                            break;
                        }
                        arr[i]--;
                }
        }

       for(int i=0;i<size;i++)
        {
        cout<<"case #"<<(i+1)<<": "<<arr_tidy[i]<<endl;
        }

    return 0;
}

int digitsNum(int x)
{
int digits=0;
while(x>0)
{
x=x/10;
digits++;
}
return digits;
}


int is_tidy(int digits,int num)
{
        int x,prev_x=10;
        bool tidy=true;
        for(int i=0;i<digits;i++)
        {
        x=num%10;
        if(prev_x<x)tidy=false;
        num=num/10;
        prev_x=x;
        }
        if(tidy==true)return true;
        else return false;
}

