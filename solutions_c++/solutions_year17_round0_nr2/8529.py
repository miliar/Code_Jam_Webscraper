#include <iostream> 
#include <vector>
#include <deque>
#include <string> 
#include <unordered_map> 
#include <unordered_set>
#include <cmath>

using namespace std;

bool isTidy(unsigned int val);
unsigned int countDigits(unsigned long N);
unsigned long lastTidy(unsigned long N);

unsigned int ones(unsigned long N);
vector<unsigned int> numToVec(unsigned long N);
void modify(vector<unsigned int> &vec);
unsigned long vecToNum(vector<unsigned int> &vec);

int main()
{
    unsigned short T;
    cin >> T;
    
    for (unsigned int i = 1; i <= T; ++i)
    {
        unsigned long N;
        cin >> N;
        cout << "Case #" << i << ": " << lastTidy(N) << endl;
    }
    
    
}

bool isTidy(unsigned int val)
{
    unsigned int temp;
    while (val != 0)
    {
        temp = (val % 10);
        val /= 10;
        if (temp < (val%10))
            return false;
    }
    return true;
}

unsigned int countDigits(unsigned long N)
{
    unsigned int result = 0;
    
    while (N != 0)
    {
        ++result;
        N /= 10;
    }
    
    return result;
}

unsigned long lastTidy(unsigned long N)
{
    vector<unsigned int> vec = numToVec(N);
    modify(vec);
    return vecToNum(vec);
}


unsigned int ones(unsigned long N)
{
    return (N % 10);
}

vector<unsigned int> numToVec(unsigned long N)
{
    vector<unsigned int> result;
    
    while (N != 0)
    {
        result.push_back(ones(N));
        N /= 10;
    }
    
    reverse(result.begin(), result.end());
    return result;
}

void modify(vector<unsigned int> &vec)
{
    for (unsigned int i = (vec.size()-1); i >= 1; --i)
    {
        if (vec[i-1] > vec[i])
        {
            --vec[i-1];
            for (unsigned int j = i; j < vec.size(); ++j)
            {
                vec[j] = 9;
            }
        }
    }
}

unsigned long vecToNum(vector<unsigned int> &vec)
{
    unsigned long result = 0;
    
    for (unsigned int i = 0; i < vec.size(); ++i)
    {
        result += vec[i];
        result *= 10;
    }
    
    return result/10;
}
