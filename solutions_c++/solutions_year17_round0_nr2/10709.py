#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    fstream files, answer;
    files.open("B-small-attempt2.in", fstream::in | fstream::out);
    answer.open("Tidy.out", fstream::trunc | fstream::in | fstream::out);
    int loop;
    files >> loop;
    //Repeat for number of loop
    for(int cases = 1; cases <= loop; ++cases)
    {
        long int input, temp, i = 0;
        files >> input;
        //Divide by 10 until zero
        bool correctness = false;
        temp = input;
        while(!correctness && temp > 0)
        {
            int prev = 9, now;
            correctness = true;
            while(temp != 0)
            {
                now = temp % 10;
                temp /= 10;
                if(now > prev) {correctness = false; break;}
                prev = now;
            }
            ++i;
            temp = input - i;
        }
        answer << "Case #" << cases << ": " << temp+1 << endl;
    }



    return 0;
}
