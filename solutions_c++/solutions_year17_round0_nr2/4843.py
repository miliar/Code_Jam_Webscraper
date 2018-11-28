#include <iostream>

bool decr(char &c)
{
    bool sub = false;
    if (c == '0')
    {
        c = '9';
        sub = true;
    }
    c -= 1;
    return sub;
}


void testcase(int n)
{
    std::string nums;
    std::cin>>nums;
    bool sub = false;
    bool reset = false;

    size_t len = nums.size();
    for (int i = len - 2; i >= 0; --i)
    {
        if (sub)
        {
            sub = decr(nums[i]);
        }

        if (nums[i] > nums[i+1])
        {
            decr(nums[i]);
            for(int j = i+1; j < len; j++)
                nums[j] = '9';
        }
    }

    std::cout<<"Case #"<<n<<": ";
    for (int i = 0; i < len; ++i)
        if(nums[i] != '0')
            std::cout<<nums[i];

    std::cout<<std::endl;
}


int main()
{
    int N;
    std::cin>>N;
    for (auto n = 1; n <= N; ++n)
        testcase(n);

    std::cout.flush();
    return 0;
}
