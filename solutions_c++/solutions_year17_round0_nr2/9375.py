#include <iostream>
#include <string>

using namespace std;

int numlen;

void print(int a[])
{
    int zero = 0;
    for(int i = 0 ; i < numlen ; i++)
    {
        if( a[i] == 0 && zero == 0 )
        {
            continue;
        }
        else
        {
            zero = 1;
            cout << a[i];
        }
    }
    cout << endl;
}

int main()
{
    int test; cin >> test;
    for (int i = 0; i < test; i++)
    {
        numlen = 0;
        int num[20],printed = 0;
        string temp; cin >> temp; 
        while( numlen < temp.length() )
        {
            num[numlen] = temp[numlen] - '0'; numlen++;
        }
        int mark = 0,j = 1;
        cout << "Case #" << i+1 << ": ";
        for( ; j < numlen ; j++)
        {
            if( num[j] < num[mark] )
            {
                num[mark]--;
                for(int k = 0 ; k < numlen ; k++)
                {
                    if(k > mark)
                    num[k] = 9;
                }
                print(num); printed = 1; break;
            }
            else if( num[j] == num[mark] )
            {
                continue;
            }
            mark++;
        }
        if(!printed)
            print(num); 
    }
    
}