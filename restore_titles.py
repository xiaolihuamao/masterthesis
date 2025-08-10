import re
import os

def restore_title_format(title):
    """恢复标题到原来的格式，保持专有名词和重要词汇的大写"""
    if not title:
        return title
    
    # 定义需要保持大写的词汇
    uppercase_words = {
        'maxwell', 'kelvin-voigt', 'rheology', 'morphology', 'development', 'advanced', 
        'processing', 'thermoplastic', 'polymer', 'materials', 'review', 'attention',
        'neural', 'information', 'processing', 'systems', 'machine', 'learning',
        'deep', 'conditional', 'generative', 'models', 'phrase', 'representations',
        'rnn', 'encoder', 'decoder', 'statistical', 'translation', 'structure',
        'time', 'long', 'short-term', 'memory', 'lstm', 'gradient-based',
        'document', 'recognition', 'convolutional', 'networks', 'analysis',
        'applications', 'prospects', 'viscoelastic', 'fluid', 'flows', 'multiscale',
        'simulations', 'complex', 'flow', 'polymers', 'rotational', 'rheometry',
        'polymer', 'melts', 'global', 'well-posedness', 'n-dimensional',
        'compressible', 'oldroyd-b', 'damping', 'mechanism', 'coupling',
        'molecular', 'chain', 'additives', 'cable', 'insulating', 'constitutive',
        'rouse', 'spring', 'stiffness', 'bead', 'friction', 'brownian',
        'intensity', 'dynamics', 'hierarchical', 'atomistic', 'coarse-grained',
        'slip-spring', 'graph-based', 'systematic', 'molecular', 'coarse-graining',
        'data-driven', 'smoothed', 'particle', 'hydrodynamics', 'governing',
        'equations', 'nonlinear', 'dynamical', 'fluid', 'mechanics', 'property',
        'prediction', 'optimization', 'polymeric', 'nanocomposites', 'state-of-the-art',
        'molecular', 'liquids', 'ionic', 'liquid', 'water', 'mixtures', 'semi-supervised',
        'just-in-time', 'mooney', 'viscosity', 'industrial', 'rubber', 'mixing',
        'synthetic', 'oil-based', 'mud', 'structure-property', 'relationships',
        'science', 'understanding', 'modeling', 'schemes', 'algorithms', 'behavior',
        'boundary', 'elements', 'clustering', 'computational', 'mechanics',
        'hydrodynamics', 'modelling', 'sparse', 'identification', 'academy',
        'sciences', 'national', 'proceedings', 'international', 'journal',
        'molecular', 'sciences', 'transactions', 'neural', 'networks', 'learning',
        'systems', 'ieee', 'proceedings', 'publisher', 'academic', 'press',
        'springer', 'nature', 'singapore', 'association', 'computational',
        'linguistics', 'mit', 'press', 'curran', 'associates', 'inc', 'aip',
        'publishing', 'mdpi', 'acs', 'publications', 'korea-australia',
        'rheology', 'journal', 'annual', 'review', 'fluid', 'mechanics',
        'cognitive', 'science', 'neural', 'computation', 'polymers', 'physics',
        'fluids', 'macromolecules', 'chemical', 'theory', 'computation'
    }
    
    # 分割成单词
    words = title.split()
    restored_words = []
    
    for word in words:
        # 检查是否在需要大写的词汇列表中
        if word.lower() in uppercase_words:
            # 保持大写
            restored_words.append(word)
        elif word.lower() in ['a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'the']:
            # 介词、冠词等小写
            restored_words.append(word.lower())
        elif word.isupper() and len(word) > 1:
            # 保持缩写词大写
            restored_words.append(word)
        elif '-' in word:
            # 处理连字符分隔的单词
            parts = word.split('-')
            restored_parts = []
            for part in parts:
                if part.lower() in uppercase_words:
                    restored_parts.append(part)
                else:
                    restored_parts.append(part.lower())
            restored_words.append('-'.join(restored_parts))
        else:
            # 其他单词首字母大写
            if word:
                restored_words.append(word[0].upper() + word[1:].lower())
            else:
                restored_words.append(word)
    
    return ' '.join(restored_words)

def process_bib_file(file_path):
    """处理单个bib文件"""
    print(f"正在恢复文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式找到所有title字段
    title_pattern = r'title\s*=\s*\{([^}]*)\}'
    
    def replace_title(match):
        title_content = match.group(1)
        restored_title = restore_title_format(title_content)
        return f'title = {{{restored_title}}}'
    
    # 替换所有title字段
    new_content = re.sub(title_pattern, replace_title, content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"完成恢复: {file_path}")

def main():
    """主函数"""
    bib_directory = "biblibrary"
    
    # 获取所有bib文件
    bib_files = [
        os.path.join(bib_directory, "jichuliubian.bib"),
        os.path.join(bib_directory, "deeplearning.bib"),
        os.path.join(bib_directory, "deepbengou.bib"),
        os.path.join(bib_directory, "shuzhimoni.bib")
    ]
    
    print("开始恢复bib文件中的论文标题格式...")
    
    for bib_file in bib_files:
        if os.path.exists(bib_file):
            process_bib_file(bib_file)
        else:
            print(f"文件不存在: {bib_file}")
    
    print("所有bib文件恢复完成！")

if __name__ == "__main__":
    main() 