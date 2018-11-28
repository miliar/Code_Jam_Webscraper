#include "number.h"

#include <assert.h>

Number::Number(uint64_t val)
{
  assert(val > 0);
  while(val > 0)
  {
    digits_.push_back(val % 10);
    val /= 10;
  }
}

uint64_t Number::ToInt()
{
  uint64_t result=0;
  
  for(auto digit=digits_.rbegin(); digit!=digits_.rend(); digit++)
  {
    result *= 10;
    result += *digit;
  }

  return result;
}

void Number::Calculate()
{
  auto pos=digits_.rbegin();
  auto posli = pos;
  auto lpos = pos;
  
  for(;pos!=digits_.rend();pos++)
  {
    if(*pos > *posli)
      posli = pos;

    if(*lpos > *pos)
      break;

    lpos = pos;    
  }

  if(pos == digits_.rend())
    return;

  (*posli)--;
  for(auto i=posli+1; i!=digits_.rend();i++)
    *i=9;
    
}
