#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int k = 0;

int findMinOperation(string str, int index)
{
    if(index == str.size())
    {
        std::size_t found = str.find('-');
        if(found != std::string::npos)
            return (int)10e5;
        else
            return 0;
    }


    int choice1 = findMinOperation(str, index + 1);
    int choice2 = (int)10e5;
    if( index + k <= str.size())
    {
       for(int i = 0 ; i < k ; ++i)
        {
            if(str[index + i] == '+')
                str[index + i] = '-';
            else
                str[index + i] = '+';
        }
        choice2 = findMinOperation(str, index + 1) + 1;
    }


    return min(choice1,choice2);
}

int main()
{
    std::ifstream in("A-small-attempt2.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    string str;
    int testcases;
    cin>>testcases;
    for(int i = 1 ; i <= testcases; ++i)
    {
        cin>>str>>k;
        int minNum = findMinOperation(str,0);

        //cout << str << endl;
        if(minNum >= (int)10e5)
        {
            cout<< "Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }
        else
        {
           cout<< "Case #"<<i<<": "<<minNum<<endl;
        }


    }

    return 0;
}
