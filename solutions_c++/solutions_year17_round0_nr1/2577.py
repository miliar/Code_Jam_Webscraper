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
    scanf("%d" ,&Case);

    bool flag;
    char in;
    int  count;
    int  num;
    int  flip;
    int  check;
    int  cake[1005];

    char filename[]="A.txt";
    fstream fp;
    fp.open(filename, ios::out);

    for(int c=0 ;c<Case ;c++)
    {
        flag = true;
        count = 0;

        while(flag)
        {
            scanf("%c" ,&in);

            if(in == '+')
            {
                cake[count] = 1;
                count++;
            }
            else if(in == '-')
            {
                cake[count] = 0;
                count++;
            }
            else if(in == ' ')
            {
                flag = false;
            }
        }

        scanf("%d" ,&num);
        flip = 0;

        if(num == 0)
        {
            //printf("Case #%d: IMPOSSIBLE\n" ,c+1);
            fp << "Case #" << c+1 << ": IMPOSSIBLE\n";
        }
        else if(num == 1)
        {
            for(int i=0 ;i<count ;i++)
            {
                if(cake[i] == 0)
                {
                    flip ++;
                }
            }
            //printf("Case #%d: %d\n" ,c+1 ,flip);
            fp << "Case #" << c+1 << ": " << flip <<"\n";
        }
        else
        {
            for(int i=0 ;i<=count-num ;i++)
            {
                if(cake[i] == 0)
                {
                    for(int j=0 ;j<num ;j++)
                    {
                        if(cake[i+j] == 0)
                        {
                            cake[i+j] = 1;
                        }
                        else
                        {
                            cake[i+j] = 0;
                        }
                    }
                    flip ++;
                }

                check = 1;
                for(int j=i ;j<count ;j++)
                {
                    check *= cake[j];
                    if(check == 0)
                    {
                        j=count;
                    }
                }

                if(check == 1)
                {
                    i = count+1;
                    //printf("Case #%d: %d\n" ,c+1 ,flip);
                    fp << "Case #" << c+1 << ": " << flip <<"\n";
                }
                
                if(i == count-num)
                {
                    //printf("Case #%d: IMPOSSIBLE\n" ,c+1);
                    fp << "Case #" << c+1 << ": IMPOSSIBLE\n";
                }
            }
        }
    }

fp.close();
return 0;
}