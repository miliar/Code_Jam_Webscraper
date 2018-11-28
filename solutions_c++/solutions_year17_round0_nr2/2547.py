#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{
    int Case;
    char in;
    scanf("%d" ,&Case);
    scanf("%c" ,&in);
    
    int num;
    int count;
    int arr[20];
    bool flag;
    
    char filename[]="B.txt";
    fstream fp;
    fp.open(filename, ios::out);

    for(int c=0 ;c<Case ;c++)
    {
        flag =true;
        count = 0;
        
        while(flag)
        {
            scanf("%c" ,&in);

            if(in == '\n')
            {
                flag = false;
            }
            else
            {
                arr[count] = in-'0';
                count ++;
            }
        }

        for(int i=0 ;i<count-1 ;i++)
        {
            if( arr[i] > arr[i+1] )
            {
                for(int j=i+1 ;j<count ;j++)
                {
                    arr[j] = 9;
                }

                arr[i] = arr[i] -1;

                i=-1;
            }
        }

        for(int i=0 ;i<count ;i++)
        {
            if(arr[i] != 0)
            {
                num = i;
                i = count+1;
            }
        }

        //cout << "Case #" << c+1 << ": ";
        fp << "Case #" << c+1 << ": ";
        for(int i=num ;i<count ;i++)
        {
             //cout << arr[i];
             fp << arr[i];
        }
        //cout << endl;
        fp << "\n";
    }

return 0;
}