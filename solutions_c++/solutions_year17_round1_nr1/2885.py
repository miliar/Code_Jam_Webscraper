#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>
#include <cstddef>
#include <limits>
#include <cassert>
#include <map>

using namespace std;

namespace 
{
    template<typename T>
    class Matrix
    {
    public:
        Matrix(std::size_t rows, std::size_t columns, const T &init = T())
            :data((rows == 0 ||
                    std::numeric_limits<std::size_t>::max()/rows >= columns)
                ?rows*columns:throw std::invalid_argument(
                    "invalid dimensions"), init),
            row_count(rows), column_count(columns) {}
        T &ix(std::size_t row, std::size_t column)
        {
            if(row >= row_count)
                throw std::invalid_argument("invalid row");
            if(column >= column_count)
                throw std::invalid_argument("invalid column");
            return data[row*column_count + column];
        }
        const T &ix(std::size_t row, std::size_t column) const
        {
            return const_cast<Matrix*>(this)->ix(row, column);
        }
        std::size_t rows() const{return row_count;}
        std::size_t columns() const{return column_count;}
    private:
        typedef std::vector<T> DataCollection;
        DataCollection data;
        std::size_t row_count;
        std::size_t column_count;
    };
    
    using CharMatrix = Matrix<char>;

    CharMatrix solve(const CharMatrix &m)
    {
        using PosMap = map<char, pair<size_t, size_t>>;
        PosMap begins;
        PosMap ends;
        CharMatrix res(m.rows(), m.columns(), '?');
        for(size_t i =0; i < m.rows(); ++i)
        {
            for(size_t j =0; j < m.columns(); ++j)
            {
                if(m.ix(i,j )== '?')
                    continue;
                const auto pos = make_pair(i, j);
                const auto curVal = m.ix(i, j);
                res.ix(i, j) = m.ix(i, j);
                {
                    auto iter = begins.find(curVal);
                    if(iter != end(begins))
                    {
                        begins[curVal] = make_pair(
                            min((iter->second).first, i),
                            min((iter->second).second, j)
                            );
                    }
                    else
                    {
                        begins.insert(make_pair(curVal, pos));
                    }
                }
                {
                    auto iter = ends.find(curVal);
                    if(iter != end(ends))
                    {
                        ends[curVal] = make_pair(
                            max((iter->second).first, i),
                            max((iter->second).second, j)
                            );
                    }
                    else
                    {
                        ends.insert(make_pair(curVal, pos));
                    }
                }
            }
        }
        for(auto &p : begins)
        {
            auto endsIter = ends.find(p.first);
            assert(endsIter != end(ends));
            for(size_t k = 0; k <= max(res.rows(), res.columns()); ++k)
            {
                if((p.second).first > 0)
                {
                    bool found = true;
                    for(size_t i = (p.second).second; i <= (endsIter->second).second; ++i)
                    {
                        if(res.ix((p.second).first-1, i) != '?')
                        {
                            found = false;
                            break;
                        }
                    }
                    if(found)
                    {
                        --((p.second).first);
                    }
                }
                if((endsIter->second).first+1 < res.rows())
                {
                    bool found = true;
                    for(size_t i = (p.second).second; i <= (endsIter->second).second; ++i)
                    {
                        if(res.ix((endsIter->second).first+1, i) != '?')
                        {
                            found = false;
                            break;
                        }
                    }
                    if(found)
                    {
                        ++((endsIter->second).first);
                    }
                }
                if((p.second).second > 0)
                {
                    bool found = true;
                    for(size_t i = (p.second).first; i <= (endsIter->second).first; ++i)
                    {
                        if(res.ix(i, (p.second).second-1) != '?')
                        {
                            found = false;
                            break;
                        }
                    }
                    if(found)
                    {
                        --((p.second).second);
                    }
                }
                if((endsIter->second).second+1 < res.columns())
                {
                    bool found = true;
                    for(size_t i = (p.second).first; i <= (endsIter->second).first; ++i)
                    {
                        if(res.ix(i, (endsIter->second).second+1) != '?')
                        {
                            found = false;
                            break;
                        }
                    }
                    if(found)
                    {
                        ++((endsIter->second).second);
                    }
                }
            }
            for(size_t i = (p.second).first; i <= (endsIter->second).first; ++i)
            {
                for(size_t j = (p.second).second; j <= (endsIter->second).second; ++j)
                {
                    res.ix(i, j) = p.first;
                }
            }
        }
        return res;
    }
}

int main()
{
    int t = 0;
    cin>>t;
    for(int i = 0; i < t; ++i)
    {
        int r = 0;
        int c = 0;
        cin>>r>>c;
        cin.ignore(1);
        CharMatrix task(r, c);
        for(int j = 0; j < r; ++j)
        {
            string str;
            getline(cin, str);
            assert(str.size() == c);
            for(int k = 0; k < c; ++k)
            {
                task.ix(j, k) = str[k];
            }
        }
        const auto res = solve(task);
        cout<<"Case #"<<i+1<<": "<<endl;
        for(size_t j = 0; j < res.rows(); ++j)
        {
            for(size_t k = 0; k < res.columns(); ++k)
            {
                cout<<res.ix(j, k);
            }
            cout<<endl;
        }
    }
    return 0;
}
