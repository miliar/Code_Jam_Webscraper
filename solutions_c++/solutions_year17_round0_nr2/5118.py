#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<sys/mman.h>

using namespace std;

#define VNAME(x) #x

const int PAGE_SHIFT = 12;
const int INPUT_MAXSIZE = 1;
const int DECIMAL_BASE = 10;
const char* LINE = "%s\n";
const char* HEADER = "Case #%d: ";

typedef struct {
  long long lhs;
  long long rhs;
  long long value;
  char word;
  char nullSign;
} digitBuffer;

static inline int pagesize() {
  return INPUT_MAXSIZE*(1 << PAGE_SHIFT);
}

static inline int getmemflags() {
  return MAP_ANONYMOUS|MAP_PRIVATE|MAP_NORESERVE|MAP_LOCKED;
}

static inline int parseInteger() {
  static int res = 0;
  scanf("%d", &res);
  return res;
}

static inline void showLong(long long value) {
  printf("%lld", value);
}

static inline void parseNewline() {
  scanf("\n");
}

static inline void showNewline() {
  printf("\n");
}

static inline char* allocateBuffer() { 
  void* result = mmap(NULL, pagesize(), PROT_READ|PROT_WRITE, getmemflags(), -1, 0);
  if(result == MAP_FAILED) {
    printf(VNAME(MAP_FAILED));
    showNewline();
    _exit(EXIT_FAILURE);
  }
  return (char*)result;
}

static inline const char* parseLine() {
  static char* const inputBuffer = allocateBuffer();
  scanf(LINE, inputBuffer);
  return inputBuffer;
}

static inline void showHeader(int testCaseId) {
  printf(HEADER, testCaseId); 
}

static inline long long getDigit(const char* input, char* buffer, int position) {
  buffer[0] = input[position];
  return (long long)atoi(buffer);
}

static inline long long decimalPower(int exp) {
  long long result = 1;
  while(exp > 0) {
    result *= DECIMAL_BASE;
    --exp;
  }
  return result;
}

static inline long long getResult(long long value, int exp) {
  long long power = decimalPower(exp);
  return power*value+power-1;
}

static inline bool update(digitBuffer* buffer) {
  bool result = (buffer->lhs <= buffer->rhs);
  if(result) {
    buffer->value = DECIMAL_BASE*buffer->value+buffer->rhs;
  }
  else {
    --buffer->value;
  }
  return result;
}

static inline long long findValue(digitBuffer* buffer, const char* input, int length) {  
  int i = 0;
  for(i=length-2; i>=0; --i) {
    buffer->rhs = buffer->lhs;
    buffer->lhs = getDigit(input, &buffer->word, i);
    if(buffer->lhs >= buffer->rhs) {      
      buffer->value /= DECIMAL_BASE;
      --buffer->value;
    }
    else {
      break;
    }   
  }
  return getResult(buffer->value, length-i-2);
}

static inline long long process(const char* input, int length) {  
  static digitBuffer* const buffer = (digitBuffer*) allocateBuffer();  
  buffer->rhs = getDigit(input, &buffer->word, 0);
  buffer->value = buffer->rhs;
  for(int i=1; i<length; ++i) {
    buffer->lhs = buffer->rhs;
    buffer->rhs = getDigit(input, &buffer->word, i);    
    if(!update(buffer)) {      
      buffer->value = getResult(findValue(buffer, input, i), length-i);
      break;
    }
  }  
  return buffer->value;
}

static inline void execute() {
  const char* inputBuffer = parseLine();
  long long result = process(inputBuffer, strlen(inputBuffer));
  showLong(result);
}

static inline int run(int tests) {
  parseNewline();
  for(int i=1; i<=tests; ++i) {
    showHeader(i);
    execute();
    showNewline();
  }
  return EXIT_SUCCESS;
}

int main() {
  int amount = parseInteger();
  return run(amount);
}
