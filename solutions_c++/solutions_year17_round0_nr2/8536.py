#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

bool isTidy(int n)
{
    deque<int> digits;
    while (n > 0)
    {
        int a = n % 10;
        digits.push_front(a);
        n /= 10;
    }
    bool isIt = true;
    for (int i = 0; i < digits.size() -1; ++i)
    {
        //cout << "checking digits " << digits[i] << " and " << digits[i+1] << endl; 
        if (digits[i] > digits[i + 1])
        {
            //cout << "violation at digit " << i << endl;
            isIt = false;
        }
    }
    return isIt;
}


int main()
{
    string input = "100 132 1000 7 241 559 803 477 994 665 401 312 247 646 166 666 545 901 204 570 720 54 828 71 917 718 763 988 452 999 1 599 227 621 361 815 432 859 305 280 772 624 779 592 245 142 65 129 335 5 334 652 235 674 447 784 715 351 639 104 134 655 746 346 552 225 949 791 223 759 969 602 540 310 993 679 795 749 590 609 733 25 589 470 21 471 628 649 926 834 394 597 884 778 437 453 564 521 321 221 661  ";
    stringstream ss(input);
    int t;
    ss >> t;
    std::vector<int> ns;
    int maxn = 0;
    for (int i = 1; i <= t; ++i)
    {
       int a; ss >> a;
       ns.push_back(a);
       maxn = max(maxn, a);
    }
    std::vector<int> lastTidy(maxn + 1 ,-1);
    int maxTidySoFar = 1;
    for (int n = 1; n <= maxn; ++n)
    {
        if (isTidy(n))
        {
            maxTidySoFar = n;
        }
        lastTidy[n] =  maxTidySoFar;
    }
    for (int i = 1; i <= t; ++i)
    {
       cout << "Case #" << i << ": " << lastTidy[ns[i -1]] << endl;
    }    
}