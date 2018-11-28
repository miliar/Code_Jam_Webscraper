#include <iostream>
#include <fstream>

using namespace std;

static long long int testCase, num, temp, num1, num2, ans, front, back;
static int pos;

ifstream fin("B-large.in");
ofstream fout("output.txt");

int main(void)
{
    fin >> testCase;
    
    for (int i = 0; i < testCase; i++)
    {
        fin >> num;
        
        num1 = 10;
        num2 = 10;
        pos = 0;
        ans = temp = num;
        
        for (int cnt = 1; temp ; cnt++)
        {
            if (num2 == 10) num2 = temp % 10;
            else num2 = num1;
                
            num1 = temp % 100;
            num1 /= 10;
                
                
            temp /= 10;
                
            if (num1 > num2)
            {
                pos = cnt;
                num1--;
            }
        }
        
        if (pos != 0)
        {
            front = 10;
            back = 1;
            
            for (int i = 1; i < pos; i++)
            {
                front *= 10;
                back *= 10;
                back += 1;
            }
            
            back *= 9;
            ans = num / front;
            ans -= 1;
            ans *= front;
            ans += back;
        }
        
        else ans = num;
        
        fout << "Case #" << i + 1 << ": " << ans << endl;
    }
    
    return 0;
}
